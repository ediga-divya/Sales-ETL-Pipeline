CREATE TABLE dim_customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE dim_product (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    subcategory VARCHAR(100)
);

CREATE TABLE fact_sales (
    sale_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    sale_date DATE,
    region VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount DECIMAL(10,2),
    total_sales DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);