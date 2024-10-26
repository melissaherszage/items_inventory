CREATE TABLE IF NOT EXISTS "2024_melissa_herszage_schema".l1_item_prices
(
    item_id            varchar(256),
    condition          varchar(256),
    price              int,
    currency           varchar(256),
    available_quantity int,
    created_at         timestamp
);