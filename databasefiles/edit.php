<?php

require "init.php";

if(isset ($_GET['edit']))
{
        $id = $_GET['edit'];
        $sql = "SELECT * FROM teatable WHERE tea_id='$id'";
        $result = mysqli_query($con, $sql);
        if (!$result) {
            die('Invalid query: ' . mysqli_error($con));
        }
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC); 
}

if( isset($_POST['new_name_of_tea']) )
{
    $newName = $_POST['new_name_of_tea'];
    $id  	 = $_POST['tea_id'];
    $sql     = "UPDATE teatable SET name_of_tea='$newName' WHERE tea_id='$id'";
    $res 	 = mysqli_query($con, $sql) 
                                or die("Could not update".mysql_error());
    echo "<meta http-equiv='refresh' content='0;url=brewtea.php'>";
}

?>

<form action="edit.php" method="POST">
Name: <input type="text" name="new_name_of_tea" value="<?php echo $row["name_of_tea"];  ?>"/>
<br />
<input type="hidden" name="tea_id" value="<?php echo $row["tea_id"]; ?>"/>
<input type="submit" value=" Update "/>
</form>


<?php
mysqli_close($con);

?>