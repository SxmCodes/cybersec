# Task 9 - Get aHEAD

**Question**
1. We are given this url ``` http://mercury.picoctf.net:28916```


**Answer**
1. We gone there and saw the souce code.
```html
<!doctype html>
<html>
<head>
    <title>Red</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<style>body {background-color: red;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
						<!-- We can give a get request. -->
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<!-- We can give a post request. -->
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```


2. We used this command ```curl -I HEAD -i http://mercury.picoctf.net:28916/index.php ```

3. We got the flag.
```
 picoCTF{r3j3ct_th3_du4l1ty_70bc61c4}
```
