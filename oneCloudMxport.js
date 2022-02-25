import { execFile } from 'child_process';
export var balanceOneCloudMxport;
execFile('python', ['oneCloudMxport.py'], (error, stdout, stderr) => {
	if (error) {
		console.error(`exec error: ${error}`);
		return;
	}
	//console.log(stdout);
	balanceOneCloudMxport = stdout;
	//console.error(`stderr: ${stderr}`);
});
