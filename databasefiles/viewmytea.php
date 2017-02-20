<?php

require "init.php";

/*
 * For quick viewing of entries in the teatable table
 * and for people who cannot access phpmyadmin i.e. localhost
 *
 */


$sql = "SELECT tea_id, name_of_tea, device_id FROM teatable";
$result = mysqli_query($con, $sql);


if(mysqli_num_rows($result) > 0)
{
    while( $row = mysql_fetch_array($result) )
    {
        echo "$row[tea_id]. $row[name_of_tea]. $row[device_id]. <a href = 'edit.php?edit=$row[tea_id]' >edit</a><br /> ";    
    }

}


else
{
    echo "0 results";
}

mysqli_close($con);

?>