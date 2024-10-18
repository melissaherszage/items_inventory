CREATE TABLE IF NOT EXISTS item_prices
(
    item_id            varchar(256),
    price              integer,
    currency           varchar(256),
    available_quantity integer,
    created_at         timestamp
);