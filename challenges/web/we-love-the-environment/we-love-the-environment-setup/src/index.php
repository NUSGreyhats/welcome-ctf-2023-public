<?php
if (!isset($_GET['prog']) || !isset($_GET['var']) || !isset($_GET['val'])) {
    highlight_file(__FILE__);
    die();
}
putenv($_GET['var'] . '=' . $_GET['val']);
passthru(escapeshellarg($_GET['prog']) . ' 2>&1');