<?php

require "init.php";

$sql = "SELECT tea_id, name_of_tea, device_id FROM teatable";
$result = mysqli_query($con, $sql);

if(mysqli_num_rows($result) > 0)
{           
                    echo "<table border=1px solid black; border-collapse:collapse; padding: 105px;>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                        <th>Device</th>
                        <th>Name Your Tea!</th>
                    </tr>";
    while($row = mysqli_fetch_assoc($result))
    {
       // echo "<tr><td>".$row["tea_id"]."</td><td>".$row["name_of_tea"]." ".$row["device_id"]." <a href = 'edit.php?edit=$row[tea_id]' >edit</a><br /> </td></tr>";   
        echo "<tr>";
        echo "<td>" . $row["tea_id"] . "</td>";
        echo "<td>" . $row["name_of_tea"] . "</td>";
        echo "<td>" . $row["device_id"] . "</td>";
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