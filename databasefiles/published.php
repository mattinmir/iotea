<?php

require "init.php";

/*
 * Print tea specs from database by fetching specified tea_id 
 * in url through GET method
 */

if (isset($_GET['download']))
{
    $id = $_GET['download'];

   //Debugging query to insert into new table of published teas
   //teapublish table used for automatic publishing of .tea file to MQTT broker <---TODO

    /*$sql = "INSERT INTO teapublish (`tea_id`,`name_of_tea`, `type_of_tea`, `device_id`,`broad_lux`,`ir_lux`,`temperature`) 
            SELECT `tea_id`, `name_of_tea`, `type_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature` FROM teanamed WHERE `tea_id` = '$id' AND 
            NOT EXISTS (SELECT * FROM teapublish WHERE `tea_id` = teanamed.tea_id);";*/



    $sql = "SELECT name_of_tea, broad_lux, temperature FROM teanamed WHERE tea_id = '$id';";
    


    $res = mysqli_query($con, $sql) 
                                or die("Could not update".mysql_error());
                                

    //Simple extraction of entry
    //Update specs to screen

    while($row = mysqli_fetch_assoc($res))
    {


        echo "<br/>";
        echo "<h1>Your .tea file</h1>";
        echo "<table border=1px solid black; border-collapse:collapse; padding: 105px;>
                    <tr>
                        <th>Name</th>
                        <th>Opacity</th>
                        <th>Temperature</th>
                    </tr>";
        
                echo "<tr>";
        echo "<td>" . $row["name_of_tea"] . "</td>";
        echo "<td>" . $row["broad_lux"] . "</td>";
        echo "<td>" . $row["temperature"] . "</td>";
        echo "</tr>";
        echo "</table>"; 

    }


}


mysqli_close($con);

?>

