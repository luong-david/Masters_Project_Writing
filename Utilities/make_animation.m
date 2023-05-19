clear, clc, close all

% settings
malware_name = 'Mixed';

 % load the images
 img_dir = ['./code/fake_tests/vae_cnn_images/',malware_name,'/'];
 nImg = 55;
 images    = cell(nImg,1);
 
 for nn = 1:nImg
     images{nn} = imread([img_dir,sprintf('generated_%s_%d.png',malware_name,nn)]);
 end
 
 % create the video writer with 1 fps
 writerObj = VideoWriter([img_dir,malware_name,'_Video.avi']);
 writerObj.FrameRate = 1;
 % set the seconds per image
 secsPerImage = 1.0*ones(1,nImg);
 % open the video writer
 open(writerObj);
 % write the frames to the video
 for u=1:length(images)
     % convert the image to a frame
     frame{u} = im2frame(images{u});
     for v=1:secsPerImage(u) 
         writeVideo(writerObj, frame{u});
     end
 end
 % close the writer object
 close(writerObj);
 
all_valid = true;
flen = length(frame);
for K = 1 : flen
  if isempty(frame{K}.cdata)
    all_valid = false;
    fprint('Empty frame occurred at frame #%d of %d\n', K, flen);
  end
end
if ~all_valid
   error('Did not write movie because of empty frames')
end
