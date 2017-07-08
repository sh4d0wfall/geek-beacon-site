<?php
$data = file_get_contents("https://github.com/OSAlt");
$content = str_replace("/OSAlt", "https://github.com/OSAlt", $data);
echo $content;
?>
