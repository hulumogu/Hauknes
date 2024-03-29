﻿<html>

<head>
	<style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Style the header */
        header {
            background-color: #666;
            padding: 5px;
            text-align: center;
            font-size: 25px;
            color: white;
        }
		div.scrollmenu {
			background-color: #666;
			overflow-y: scroll;
			white-space: nowrap;
			width: 20%;
			height: calc(100vh - 50px)
		}
		div.scrollmenu a {
			color: white;
			text-align: center;
			padding: 14px;
			text-decoration: none;
		}
		div.scrollmenu a:hover {
			background-color: #777;
		}
		.scrollmenu img:hover {
			opacity: 1;
		}
		.scrollmenu img {
			opacity: 0.5;
			cursor: pointer;
		}
		/* Container for flexboxes */
		div.row {
		  display: -webkit-flex;
		  display: flex;
		}

		div.right {
		  height: 100%;
		  width: 80%;
		}

		.container {
		  position: relative;
		}

		/* Bottom right text */
		.text-block {
		  position: absolute;
		  top: 20px;
		  left: 20px;
		  background-color: black;
		  color: white;
		  padding-left: 20px;
		  padding-right: 20px;
		}
	</style>
</head>

<body>

	<header>
		<h2>Røyslia</h2>
	</header>

	<div class="row">
		<div class="scrollmenu">

		<?php
			// push all json data into a new array
			$imageDataArray = array();

			$numPictures = 0;
			for ($day_number = 0; $day_number < 10; $day_number++)
			{
				for ($hour = 0; $hour <= 23; $hour++) 
				{
					$someDaysAgo = mktime($hour, 0, 0, date("m"), date("d")-$day_number,date("Y"));
					$formatted_value = date("Y-m-d-H", $someDaysAgo);


					$time = date("H:00:00", $someDaysAgo);
					$date = date("d-m-Y", $someDaysAgo);
#				    echo "<img id='$hour' src='../images/royslia/".$formatted_value."_thumbnail.jpg' style='width:100%;' onclick='showImage(this);' data-time='".$time."' data-date='".$date."' >
#									<br>
#				";
					{
						$jsonFileName = "../images/royslia/$formatted_value.json";
						if (file_exists($jsonFileName))
						{
							$string = file_get_contents($jsonFileName);
							if ($string === false) {
								echo "file_get_contents failed";
							}

							$json_a = json_decode($string, true);
							if ($json_a === null) {
								echo "json_decode failed";
							}

							foreach ($json_a as $key => $data) 
							{
								if ($key === "imageinfo" && is_array($data))
								{
								    $rgb_average = 0;
									$temperature_inside = 0;
									$temperature_outside = 0;
									foreach ($data as $childKey => $childData) 
									{
										if (is_array($data))
										{
											// more than one application add data to json file, so add them as they coma as childs
											if (isset($childData['rgb_average']))
											{
												$rgb_average = $childData['rgb_average'];
											}

											if (isset($childData['temperature_inside']))
											{
												$temperature_inside = $childData['temperature_inside'];
												$temperature_outside = $childData['temperature_outside'];
											}
										}
									}
		
									array_push($imageDataArray, array($formatted_value, $formatted_value, $date, $time, $temperature_inside, $temperature_outside));
									$numPictures++;
								}
							}
						}
					}
				}
			}
			$numPictures--;

			rsort($imageDataArray);
	
			for ($x = 0; $x <= $numPictures; $x++) 
			{
				echo "<div class='container'>";
				echo "<img id='$x' src='../images/royslia/".$imageDataArray[$x][1]."_thumbnail.jpg' style='width:100%;' onclick='showImage(this);' data-time='".$imageDataArray[$x][3]."' data-date='".$imageDataArray[$x][2]."' data-temperature_inside='".$imageDataArray[$x][4]."' data-temperature_outside='".$imageDataArray[$x][5]."' >
				<br>
				";
				echo "<div class='text-block'>";
				echo $imageDataArray[$x][5]." ℃";
				echo "</div>";
				echo "</div>";
			}
		?>
		</div>
		<div class="right">
			<div class="container">
				<img id="expandedImg" src='../images/royslia/<?php echo $imageDataArray[0][1]; ?>.jpg' style="width:100%;" >
				<div class="text-block">
					Temperature outside : <span id="id_temperature_outside"><?php echo $imageDataArray[0][5]; ?></span> ℃<br>
					Temperature inside : <span id="id_temperature_inside"><?php echo $imageDataArray[0][4]; ?></span> ℃<br>
					Date : <span id="id_date"><?php echo $imageDataArray[0][2]; ?></span><br>
					Time : <span id="id_time"><?php echo $imageDataArray[0][3]; ?></span><br>
				</div>
			</div>
		</div>
	</div>	
	<footer>
		
	</footer>

	<script>
		var numPictures = <?php echo $numPictures; ?>;
		var selectedImage = 0;
		
		var start = null;
		window.addEventListener("touchstart",function(event)
		{
			if(event.touches.length === 1)
			{
				//just one finger touched
				start = event.touches.item(0).clientX;
			}
			else
			{
				//a second finger hit the screen, abort the touch
				start = null;
			}
		});

		window.addEventListener("touchend",function(event)
		{
			var offset = 100;//at least 100px are a swipe
			if(start)
			{
				//the only finger that hit the screen left it
				var end = event.changedTouches.item(0).clientX;


				if(end < start - offset )
				{
					var expandImg = document.getElementById("expandedImg");
					if (selectedImage < numPictures)
					{
						selectedImage++;
						var img = document.getElementById(selectedImage);
						showImage(img);
					}

				}
				else if (end > start + offset)
				{
					var expandImg = document.getElementById("expandedImg");
					if (selectedImage > 0)
					{
						selectedImage--;
						var img = document.getElementById(selectedImage);
						showImage(img);
					}
				}
			}
		});

		function showImage(imgs) 
		{
			selectedImage = imgs.id;

			// first remove style around image
			var i;
			for (i = 0; i <= numPictures; i++) 
			{
				var img = document.getElementById(i);
				img.style = "width:100%;";
			}

			var expandImg = document.getElementById("expandedImg");

			// remove thumbnail from src name
			var srcHiRes = imgs.src;
			var posSplit = srcHiRes.indexOf("_thumbnail");
			srcHiRes = srcHiRes.substring(0, posSplit);
			expandImg.src = srcHiRes + ".jpg";

			imgs.style = "width:100%;border:2px solid white";
			expandImg.parentElement.style.display = "block";
		
			var dateElem = document.getElementById("id_date");
			dateElem.innerHTML = imgs.dataset.date;
			
			var timeElem = document.getElementById("id_time");
			timeElem.innerHTML = imgs.dataset.time;

			var tempInsideElem = document.getElementById("id_temperature_inside");
			tempInsideElem.innerHTML = imgs.dataset.temperature_inside;

			var tempOutsideElem = document.getElementById("id_temperature_outside");
			tempOutsideElem.innerHTML = imgs.dataset.temperature_outside;
		}
	</script>
</body>

</html>
