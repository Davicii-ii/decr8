/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.com/docs/reference/config-files/gatsby-node/
 */

/**
 * @type {import('gatsby').GatsbyNode['createPages']}
 */

const fs = require('fs');
const path = require('path');
const nodeID3 = require('node-id3');

exports.onCreateWebpackConfig = ({ stage, loaders, actions }) => {
    if (stage === 'build-html') {
	actions.setWebpackConfig({
	    module: {
		rules: [
		    {
			test: /node-id3/,
			use: loaders.null(),
		    },
		],
	    },
	});
    }
};

exports.onPreBootstrap = ({ reporter }) => {
    const musicDir = path.resolve(__dirname, './src/music');
    const imageDir = path.resolve(__dirname, './src/images');

    // Read all mp3 files from musicDir
    fs.readdir(musicDir, (err, files) => {
	if (err) {
	    reporter.error(`Error reading music directory: ${err}`);
	    return;
	}


	// Loop through all mp3 files
	for (let i = 0; i < files.length; i++) {
	    const file = files[i];
	    const filePath = path.join(musicDir, file);

	    // Check if file is an mp3
            if (path.extname(file) !== '.mp3') {
                reporter.warn(`Skipping non-mp3 file: ${file}`);
                return;
            }

	    // Read the album art from the mp3 file
	    const tags = nodeID3.read(filePath);
	    const { image } = tags;

	    if (!image) {
		reporter.warn(`No album art found in file: ${file}`);
		continue;
	    }

	    // Save the album art to the images directory
	    const imageName = `${path.parse(file).name}.jpg`;
	    const imagePath = path.join(imageDir, imageName);
	    fs.writeFile(imagePath, image.imageBuffer, (err) => {
		if (err) {
		    reporter.error(`Error saving album art: ${err}`);
		} else {
		    reporter.success(`Saved album art to: ${imagePath}`);
		}
	    });
	};
    });
};
