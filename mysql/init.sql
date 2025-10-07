CREATE TABLE IF NOT EXISTS access_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time DATETIME,
    remote_addr VARCHAR(45),
    method VARCHAR(10),
    uri TEXT,
    status INT,
    bytes_sent INT,
    upstream_time VARCHAR(20),
    request_time FLOAT
);
