<html>

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
			background-color: #333;
			overflow: auto;
			white-space: nowrap;
		}
		div.scrollmenu a {
			display: inline-block;
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
	</style>
</head>

<body>

	<header>
		<h2>Røyslia</h2>
	</header>

	<nav>
		<div class="scrollmenu">

	<?php
//		$day_number = date('N');
		// push all json data into a new array
		$imageDataArray = array();

		$numPictures = 0;
		for ($day_number = 1; $day_number <= 7; $day_number++)
		{
			for ($x = 0; $x <= 23; $x++) 
			{
				$formatted_value = sprintf("%d_%02d", $day_number, $x);

				$time = "01:01:00";
				$date = "01/01/2011";
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
								foreach ($data as $childKey => $childData) 
								{
									if (is_array($data))
									{
										$time = $childData['time'];
										$date = $childData['date'];
										array_push($imageDataArray, array($date . '-' . $time, $formatted_value, $date, $time));
										$numPictures++;
									}
								}
							}
						}
					}
				}
			}
		}
		$numPictures--;

		// sort our $date . '-' . $time string so that we get the newest imagest first
		rsort($imageDataArray);
	
		for ($x = 0; $x <= $numPictures; $x++) 
		{
			echo "<img id='$x' src='../images/royslia/".$imageDataArray[$x][1]."_thumbnail.jpg' width='10%' height='10%' style='' onclick='showImage(this);' data-time='".$imageDataArray[$x][3]."' data-date='".$imageDataArray[$x][2]."'>
			";
		}
	?>
		</div>
	</nav>

	<article>
		<img id="expandedImg" src='../images/royslia/<?php echo $imageDataArray[0][1]; ?>.jpg' style="width:100%">
	</article>
	
	<footer>
		Date : <span id="id_date"><?php echo $imageDataArray[0][2]; ?></span><br>
		Time : <span id="id_time"><?php echo $imageDataArray[0][3]; ?></span><br>
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
				img.style = "";
			}

			var expandImg = document.getElementById("expandedImg");

			// remove thumbnail from src name
			var srcHiRes = imgs.src;
			var posSplit = srcHiRes.indexOf("_thumbnail");
			srcHiRes = srcHiRes.substring(0, posSplit);
			expandImg.src = srcHiRes + ".jpg";

			imgs.style = "border:1px solid white";
			expandImg.parentElement.style.display = "block";
		
			var dateElem = document.getElementById("id_date");
			dateElem.innerHTML = imgs.dataset.date;
			
			var timeElem = document.getElementById("id_time");
			timeElem.innerHTML = imgs.dataset.time;
		}
	</script>
</body>

</html>
