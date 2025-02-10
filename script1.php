<?php

// specify the path to the image
$imagePath = "images_final/s20.png";

// call the Python script to compute GLCM features
$command = escapeshellcmd("python glcm.py $imagePath");
$output = shell_exec($command);

// send the output excel file back to PHP
header("Content-Type: application/vnd.ms-excel");
header("Content-Disposition: attachment; filename=glcm_features.xlsx");
echo $output;

?>



