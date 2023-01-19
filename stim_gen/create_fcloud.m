function fcloud = create_fcloud(size,D)

find_b = (D*2)-6;
fcloud = spatialPattern([size,size], find_b);
end
