function fcloud_images(N, low, high, step, size)


for D = low:step:high

    for i = 1:N
        fcloud = mat2gray(create_fcloud(size,D));
        imwrite(fcloud, strcat('E:\PhD\Apophenia_Project\Stimuli_Pareidolie\fclouds_batch2\fcloud_D', num2str(D), '_',num2str(i), '.tif'));
    end
end
    
    
end
