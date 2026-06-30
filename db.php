<?php

// Database settings for Docker and local development.
// In Docker, the MySQL service is reachable by the service name `db`.
$servername = getenv('MYSQL_HOST') ?: "db";
$username = getenv('MYSQL_USER') ?: "root";
$password = getenv('MYSQL_PASSWORD') ?: "";
$db = getenv('MYSQL_DATABASE') ?: "onlineshop";

// Create connection
$con = mysqli_connect($servername, $username, $password, $db);
$conn = $con;

// Check connection
if (!$con) {
    die("Error while connecting...! " . mysqli_connect_error());
}

?>