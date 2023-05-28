<?php
/* Download from Youtbe 
pip3 install yt-dlp

yt-dlp -f bestvideo[ext=mp4]+bestaudio[ext=m4a]  --merge-output-format mkv "https://www.youtube.com/watch?v=tsOPKQ6AwN4&pp=ygUFb3NtYW4%3D"



    
yt-dlp -f bestvideo+bestaudio  --merge-output-format mkv "link to youtube video"

$naa = $argv[1];


// Replace with your own credentials
$apiKey = '779ec11d28087c2825a1';
$apiSecret = '7110b4277e7e9f46e333c79114ead86c2f6e06aa';
$testUser = 'mawiya@outlook.be';
$testPassword = 'amigr8@16D';

require_once 'Dailymotion.php';


// Scopes you need to run your tests
$scopes = array(
    'manage_videos',
);

// Dailymotion object instantiation
$api = new Dailymotion();
$api->setGrantType(
    Dailymotion::GRANT_TYPE_PASSWORD,
    $apiKey,
    $apiSecret,
    $scopes,
    array(
        'username' => $testUser,
        'password' => $testPassword,
    )
);

// 1. Upload your file on Dailymotion's servers
// Replace with the path to your video
$url = $api->uploadFile("$naa");

// 2. Create the video on your channel - Replace with your <CHANNEL_ID>
$api->post(
    '/user/x2k6ogq/videos',
    array(
        'url'       => $url,
        'title'     => $naa,
      //  'channel'   => 'urdustream',
        'published' => true,
        'is_created_for_kids' => false,
    )
);
