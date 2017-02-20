<?php

require "init.php";

/*
 * Initially print all entries in the database,
 * print "0 results" if no entries are found
 */

$sql = "SELECT tea_id, name_of_tea, time, device_id, type_of_tea, name_of_tea FROM teatable;";
$result = mysqli_query($con, $sql);

if(mysqli_num_rows($result) > 0)
{           
                    echo "<table border=1px solid black; border-collapse:collapse; padding: 105px;>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                        <th>Time</th>
                        <th>Device</th>
                        <th>Type of tea</th>
                        <th>Set a Tea Type</th>
                        <th>Name Your Tea!</th>
                    </tr>";

    //Both type_of_tea and name_of_tea initially empty for new entries
    //Entries are added by means of GET requests (edit, edditype) in edit.php and teatype.php
    while($row = mysqli_fetch_assoc($result))
    {
        echo "<tr>";
        echo "<td>" . $row["tea_id"] . "</td>";
        echo "<td>" . $row["name_of_tea"] . "</td>";
        echo "<td>" . $row["time"] . "</td>";
        echo "<td>" . $row["device_id"] . "</td>";
        echo "<td>" . $row["type_of_tea"]. "</td>";
        echo "<td> <a href = 'teatype.php?edittype=$row[tea_id]' ><button type='button'>Type of tea</button></a><br /> </td>";
        echo "<td> <a href = 'edit.php?edit=$row[tea_id]' ><button type='button'>Name me</button></a><br /> </td>";
        echo "</tr>";
    }

    echo "</table>"; 
}    
   
else
{
    echo "0 results";
}


mysqli_close($con);

?>