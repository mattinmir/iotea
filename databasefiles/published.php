<?php

require "init.php";

/*
if(isset ($_GET['download']))
{
        $id = $_GET['download'];
        $sql = "SELECT * FROM teanamed WHERE tea_id='$id'";
        $result = mysqli_query($con, $sql);
        if (!$result) {
            die('Invalid query: ' . mysqli_error($con));
        }
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC); 
}
*/

//exec(sctipy,)

if (isset($_GET['download']))
{
    $id = $_GET['download'];
    /*$sql = "INSERT INTO teapublish (`tea_id`,`name_of_tea`, `type_of_tea`, `device_id`,`broad_lux`,`ir_lux`,`temperature`) 
            SELECT `tea_id`, `name_of_tea`, `type_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature` FROM teanamed WHERE `tea_id` = '$id' AND 
            NOT EXISTS (SELECT * FROM teapublish WHERE `tea_id` = teanamed.tea_id);";*/
    $sql = "SELECT broad_lux, ir_lux, temperature FROM teanamed WHERE tea_id = '$id';";
    


    $res = mysqli_query($con, $sql) 
                                or die("Could not update".mysql_error());
   // echo "<meta http-equiv='refresh' content='0;url=printea.php'>";

   // $row = mysqli_fetch_row($res);
    while($row = mysqli_fetch_assoc($res))
    {
        $cmd = "D:\\python.exe D:\\wamp64\\www\\iotea\\brewtea.py " . $row["broad_lux"] . ' ' . $row["ir_lux"]. ' ' . $row["temperature"];
        echo $cmd;
        $output = shell_exec($cmd);
        echo $output;
        echo "woolomooolo";
        exec($cmd);
    }


}
    //echo "DOWNLOADED!";
   // $row = mysqli_fetch_array($result, MYSQLI_ASSOC); 



mysqli_close($con);

?>

<!--
<form action="published.php" method="POST">
 <button type = "submit">DOWNLOAD!</button>
</form>
-->