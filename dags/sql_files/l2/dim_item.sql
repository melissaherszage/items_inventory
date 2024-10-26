BEGIN TRANSACTION
;

CREATE TEMPORARY TABLE staging_dim_item AS
(
WITH filter_variables AS
(SELECT COALESCE(MAX(_dim_item_audit_time), '2024-10-16'::timestamp) AS last_updated FROM "2024_melissa_herszage_schema".l2_dim_item)

    SELECT id as item_id,
        title,
        created_at as _l1_audit_time,
        current_timestamp as _dim_item_audit_time
    FROM "2024_melissa_herszage_schema".l1_items as i
    CROSS JOIN filter_variables fv
    WHERE i.created_at > last_updated
    )
;

DELETE FROM "2024_melissa_herszage_schema".l2_dim_item
WHERE item_id IN (SELECT item_id FROM staging_dim_item)
;

INSERT INTO "2024_melissa_herszage_schema".l2_dim_item
(SELECT * FROM staging_dim_item)
;

END TRANSACTION
;