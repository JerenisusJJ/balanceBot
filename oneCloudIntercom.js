import { execFile } from 'child_process';
export var balanceOneCloudInrecom;
execFile('python', ['oneCloudIntercom.py'], (error, stdout, stderr) => {
	if (error) {
		console.error(`exec error: ${error}`);
		return;
	}
	//console.log(stdout);
	balanceOneCloudInrecom = stdout;
	//console.error(`stderr: ${stderr}`);
});

