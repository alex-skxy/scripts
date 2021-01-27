import {ld as _} from 'https://x.nest.land/deno-lodash@1.0.0/mod.ts';

const downloadsDir = getDownloadsDir();
const filenameToMatch = 'external-content.duckduckgo.com'

Deno.chdir(downloadsDir);
const watcher = Deno.watchFs('.');

let createEvent: Deno.FsEvent;
for await (const event of watcher) {
    if (event.kind == 'create') {
        createEvent = event;
    }
    const file = event.paths[0];
    console.log(event);
    _.debounce(async () => {
        console.log('debounce power');
        if (createEvent && file.match(filenameToMatch)) {
            const extension = getFileExtension(file);
            const newFilename = `${generateNewFilename()}.${extension}`;
            await renameFile(file, newFilename);
        }
    }, 500, {isImmediate: false});
}

async function renameFile(filename: string, newFilename: string) {
    console.log(`Found new file ${filename}. Renaming to ${newFilename}`);
    await Deno.rename(filename, newFilename);
}

function generateNewFilename(): string {
    const date = new Date();
    return `duck${date.getDay()}-${date.getMonth()}-${date.getFullYear()}` +
        `${date.getHours()}-${date.getMinutes()}-${date.getSeconds()}`;
}

function getFileExtension(filename: string): string {
    return filename.slice((Math.max(0, filename.lastIndexOf(".")) || Infinity) + 1);
}

function getDownloadsDir(): string {
    let downloadsDir;
    if (Deno.args.length == 0) {
        console.log('No directory specified... Taking default ~/Downloads');
        downloadsDir = Deno.env.get('HOME') + '/Downloads';
    } else {
        downloadsDir = Deno.args[0];
    }
    return downloadsDir;
}
