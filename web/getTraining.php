<?php
// Script to get contents of training file

if (file_exists('training.txt')) {
    header('Content-Type: text/plain');
    echo file_get_contents('training.txt');
} else {
    http_response_code(404);
    echo "Error; file not found";
}
?>