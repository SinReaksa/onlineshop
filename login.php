<?php
include "db.php";

session_start();

# Login script begins here
# If user given credentials match successfully with data available in the database, we will echo string "login_success"

if(isset($_POST["email"]) && isset($_POST["password"])){
    $email = mysqli_real_escape_string($con, $_POST["email"]);
    $password = $_POST["password"]; // Note: If users use MD5 like admins, change this to md5($_POST["password"])
    
    // 1. Check if it's a regular user
    $sql = "SELECT * FROM user_info WHERE email = '$email' AND password = '$password'";
    $run_query = mysqli_query($con, $sql);
    $count = mysqli_num_rows($run_query);
    
    if($count == 1){
        $row = mysqli_fetch_array($run_query);
        
        // FIX: Assign session variables FIRST so they are available for the code below
        $_SESSION["uid"] = $row["user_id"];
        $_SESSION["name"] = $row["first_name"];
        $ip_add = getenv("REMOTE_ADDR");
            
        // Check if user has items stored in temporary guest cookies
        if (isset($_COOKIE["product_list"])) {
            $p_list = stripcslashes($_COOKIE["product_list"]);
            $product_list = json_decode($p_list, true);
            
            for ($i=0; $i < count($product_list); $i++) { 
                // Verify if the item is already listed in user's permanent cart
                $verify_cart = "SELECT id FROM cart WHERE user_id = ".$_SESSION['uid']." AND p_id = ".$product_list[$i];
                $result  = mysqli_query($con, $verify_cart);
                
                if(mysqli_num_rows($result) < 1){
                    // Update user_id into database table with valid registered id
                    $update_cart = "UPDATE cart SET user_id = '".$_SESSION['uid']."' WHERE ip_add = '$ip_add' AND user_id = -1";
                    mysqli_query($con, $update_cart);
                } else {
                    // If already available, delete the duplicate temporary guest entry
                    $delete_existing_product = "DELETE FROM cart WHERE user_id = -1 AND ip_add = '$ip_add' AND p_id = ".$product_list[$i];
                    mysqli_query($con, $delete_existing_product);
                }
            }
            
            // Destroy the guest product list cookie
            setcookie("product_list", "", time() - 3600, "/");
            
            // AJAX callback handler expectations
            echo "cart_login";
            exit();
        }
        
        // Update user's standard guest session cart & wishlist to their account
        $sql = "UPDATE cart SET user_id = '".$_SESSION['uid']."' WHERE ip_add='$ip_add' AND user_id = -1";
        $wishlist_sql = "UPDATE wishlist SET user_id = '".$_SESSION['uid']."' WHERE ip_add='$ip_add' AND user_id = -1";
        
        mysqli_query($con, $sql);
        mysqli_query($con, $wishlist_sql);
        
        echo "login_success";
        
        // Clean redirection sequence
        if(isset($_SERVER['HTTP_REFERER']) && !empty($_SERVER['HTTP_REFERER'])) {
            echo "<script> location.href='".$_SERVER['HTTP_REFERER']."'; </script>";
        } else {
            echo "<script> location.href='index.php'; </script>";
        }
        exit();

    } else {
        // 2. Check if it's an Admin (Uses MD5 password encryption)
        $admin_password = md5($_POST["password"]);
        $sql = "SELECT * FROM admin_info WHERE admin_email = '$email' AND admin_password = '$admin_password'";
        $run_query = mysqli_query($con, $sql);
        $count = mysqli_num_rows($run_query);

        if($count == 1){
            $row = mysqli_fetch_array($run_query);
            $_SESSION["uid"] = $row["admin_id"];
            $_SESSION["name"] = $row["admin_name"];
            
            echo "login_success";
            echo "<script> location.href='admin/add_products.php'; </script>";
            exit();
        } else {
            echo "<span style='color:red;'>Please register before login..!</span>";
            exit();
        }
    }
}
?>