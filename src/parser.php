<?

$source = "ip_files";
$dest = "iptocountry";

function findFiles($dir){
	$dir = trim($dir);
	if(substr($dir,-1)!='/')
		$dir .= "/";
	$files = array();
	if (is_dir($dir)) {
    	if ($dh = opendir($dir)) {
        	while (($file = readdir($dh)) !== false) {
        		if($file == "." || $file == ".."){
        			continue;
        		}
        		switch(filetype($dir . $file)){
        			case "file":
        				if(substr($file, -4)==".php")
        					$files[] = $dir . $file;
        				break;
        			case "dir":
        				$files = array_merge($files, findFiles($dir . $file));
        				break;
        		}
        	}
        	closedir($dh);
    	}
	}
	return $files;
}

$files = findFiles($source);
foreach($files as $file){
	parseFile($file);
}

function parseFile($file){
	
	$skip = array("<?php","?>");
	
	$b = basename($file, ".php");
	//if(!is_numeric($b))
		//return;

	$data = file_get_contents($file);
	$lines = explode("\n",$data);
	$out = array();
	foreach($lines as $line){
		$line = trim($line);
		if(!strlen($line) || in_array($line, $skip))
			continue;

		// kommentaar
		if(substr($line,0,2)=="//"){
			$out[] = str_replace("//","#",$line);
			continue;
		}
		
		if(str_replace(" ","",$line)=='$ranges=Array('){
			$out[] = "ranges = {";
			continue;
		}
		//$countries=Array(
		if(str_replace(" ","",$line)=='$countries=Array('){
			$out[] = "countries = {";
			continue;
		}
		if(str_replace(" ","",$line)==');'){
			$out[] = "}";
			continue;
		}
		
		if(preg_match('/(\w+)"\s?=>\s?array\("(\w+)","([\s\w]+)"\)(,*)/s',$line,$m)){
			$out[] = sprintf('    "%s": ["%s", "%s"]%s', $m[1],$m[2],$m[3],$m[4]);
		}
		
	}

	$output = join("\n",$out);
	file_put_contents("iptocountry/ip".$b.".py",$output);
	echo "iptocountry/ip".$b.".py"." OK, ".count($out)." lines<br />";
}