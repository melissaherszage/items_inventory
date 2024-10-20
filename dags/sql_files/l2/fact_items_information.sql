BEGIN TRANSACTION
;

CREATE TEMPORARY TABLE staging_fact_items_information AS
(
WITH filter_variables AS
(SELECT COALESCE(MAX(_fact_items_information_audit_time), '2024-10-16'::timestamp) AS last_updated FROM "2024_melissa_herszage_schema".l2_fact_items_information)

    SELECT item_id,
           CASE WHEN condition = 'new' THEN 1 ELSE 2 END as condition_id,
           CASE WHEN currency = 'ARS' THEN 1 ELSE 2 END as currency_id,
           price,
           available_quantity,
           created_at as _l1_audit_time,
           current_timestamp as _fact_items_information_audit_time
        FROM "2024_melissa_herszage_schema".l1_item_prices
    )
;

DELETE FROM "2024_melissa_herszage_schema".l2_fact_items_information
WHERE item_id IN (SELECT item_id FROM staging_fact_items_information)
;

INSERT INTO "2024_melissa_herszage_schema".l2_fact_items_information
(SELECT * FROM staging_fact_items_information)
;

END TRANSACTION
;