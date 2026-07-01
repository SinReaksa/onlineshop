<?php

// Database settings for Docker and local development.
// In Docker, the MySQL service is reachable by the service name `online_shop_db`.
$servername = getenv('MYSQL_HOST') ?: "online_shop_db";
$username = getenv('MYSQL_USER') ?: "root";
$password = getenv('MYSQL_PASSWORD') ?: "root";
$db = getenv('MYSQL_DATABASE') ?: "onlineshop";

// Create connection
$con = mysqli_connect($servername, $username, $password, $db);
$conn = $con;

// Check connection
if (!$con) {
    die("Error while connecting...! " . mysqli_connect_error());
}

?>