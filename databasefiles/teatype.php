<?php

require "init.php";

/*
 * Get tea_id from url and post the new name to the database 
 * by means of an UPDATE query
 */


//Pull parameter from URL (GET)
if(isset ($_GET['edittype']))
{
        $id = $_GET['edittype'];
        $sql = "SELECT * FROM teatable WHERE tea_id='$id'";
        $result = mysqli_query($con, $sql);
        if (!$result) {
            die('Invalid query: ' . mysqli_error($con));
        }
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC); 
        $teaName = $row["name_of_tea"];
        $id = $row["tea_id"];
}

//Update tea type in table 

if( isset($_POST['new_type_of_tea']) )
{
    $newType = $_POST['new_type_of_tea'];
    $id  	 = $_POST['tea_id'];
    $sql     = "UPDATE teatable SET type_of_tea='$newType' WHERE tea_id='$id'";
    $res 	 = mysqli_query($con, $sql) 
                                or die("Could not update".mysql_error());
    echo "<meta http-equiv='refresh' content='0;url=printea.php'>";
}
 


//HTML listbox to select the new type_of_tea parameters
//and submit by a POST method

?>


<form action="teatype.php" method="POST">
<select name="new_type_of_tea">
        <option value="Green" name="new_type_of_tea">Green</option>
        <option value="Black" name="new_type_of_tea">Black</option>
        <option value="Fruit" name="new_type_of_tea">Fruit</option>
        <option value="Camamile" name="new_type_of_tea">Camamile</option>
</select>
<br />
<input type="hidden" name="tea_id" value="<?php echo $id; ?>"/>
<input type="submit" name="Update" value=" Update "/>
</form>


<?php
mysqli_close($con);

?>