<?php

require "init.php";

$sql = "INSERT INTO teanamed (`tea_id`,`name_of_tea`,`type_of_tea`,`device_id`,`broad_lux`,`ir_lux`,`temperature`) SELECT `tea_id`, `name_of_tea`, `type_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature` FROM teatable WHERE `name_of_tea`IS NOT NULL AND NOT EXISTS (SELECT * FROM teanamed WHERE `tea_id` = teatable.tea_id);";
$result = mysqli_query($con, $sql);
if(!$result)
{
    echo "Connection Error " ,mysqli_connect_error();
}

else 
{
   // echo "<h3> Database connection success </h3>";
}
        


$sql = "SELECT tea_id, name_of_tea, device_id FROM teanamed";
$result = mysqli_query($con, $sql);

if(mysqli_num_rows($result) > 0)
{           
                    echo "<table border=1px solid black; border-collapse:collapse; padding: 105px;>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                        <th>Device</th>
                        <th>Download!</th>
                    </tr>";
    while($row = mysqli_fetch_assoc($result))
    {
       // echo "<tr><td>".$row["tea_id"]."</td><td>".$row["name_of_tea"]." ".$row["device_id"]." <a href = 'edit.php?edit=$row[tea_id]' >edit</a><br /> </td></tr>";   
        echo "<tr>";
        echo "<td>" . $row["tea_id"] . "</td>";
        echo "<td>" . $row["name_of_tea"] . "</td>";
        echo "<td>" . $row["device_id"] . "</td>";
        echo "<td> <a href = 'published.php?download=$row[tea_id]' ><button type='button'>Brew</button></a><br /> </td>";
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