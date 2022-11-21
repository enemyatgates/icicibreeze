<?php
include dirname(dirname(__DIR__)) . "/O+00+00+03+ICICIBREEZE/breezeValues.php";

// // Get API Access Session Token
$token = $_POST["API_Session"];
echo "API Session Token:" . $token;

// Connect to Database
try {
    $conn = mysqli_connect($servername,$username,$password,$database);
} catch (Exception $e) {
    echo $e->getMessage();
}
 
// Verify Connection
if (!$conn) {
    echo "<h1>Error</h1><br>";
    die("Connection Failed: " . mysqli_connect_error());
} else {
    echo "<h1>Connected Successfully!</h1>";
}

// Update Table in Database
$query = "INSERT INTO icicitoken (TokenNumber) Values ($token);";
if (mysqli_query($conn,$query)) {
    echo "<h1>Record Created Successfully!</h1>";
    echo "<h1>Now, you can use functions/scripts.</h1>";
} else {
    die("Inseertion Failed: " . mysqli_error($conn));
}

// Close Connection to Database
mysqli_close($conn);
?>
