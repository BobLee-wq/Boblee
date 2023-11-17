<?

$fullname = $_POST["fullname"];
$email = $_POST["email"];
$phone_number=$_POST['phone'];
$message = $_POST["message"];

if ( ! $fullname) {
    die("Must enter a name");
}

$host = "localhost";
$dbname = "id21359423_runtimeterrorctu";
$username = "root";
$password = "";

mysqli_connect($host, $username, $password, $dbname);
// Check connection
if(mysqli_connect_errno()) {
    die("Connection failed: ".mysqli_connect_error());
}

echo "Connect was successful";
