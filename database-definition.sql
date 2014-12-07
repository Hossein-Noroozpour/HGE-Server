CREATE DATABASE IF NOT EXISTS hge;
USE hge;
CREATE TABLE IF NOT EXISTS hge_security
(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    session_key CHAR(32) CHARACTER SET UTF8 NOT NULL,
    aes_key     CHAR(16) CHARACTER SET UTF8 NOT NULL,
    aes_iv      CHAR(16) CHARACTER SET UTF8 NOT NULL,
    last_login_time DATETIME NOT NULL,
    last_try_time   DATETIME NOT NULL,
    create_time     DATETIME NOT NULL,
    login_tries INT UNSIGNED NOT NULL,
    login_state INT UNSIGNED NOT NULL
);



INSERT INTO hge_security
(
    session_key,
    aes_key,
    aes_iv,
    last_login_time,
    last_try_time,
    create_time,
    login_tries,
    login_state
)
VALUES
(
    "01234567890123456789012345678901",
    "01234567890123456789012345678901",
    "01234567890123456789012345678901",
    NOW(),
    NOW(),
    NOW(),
    0,
    0
);