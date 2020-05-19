clear all
path='D:\Cs_about\WebSite\SN&XW v1.1\images\index\gallery2';
file=dir(path);
ImgStruct={};
pathcell={};
loccell={};
for i=1:length(file)
    if length(file(i).name)>2
        subfile=[path,'\',file(i).name];
        subfile=dir(subfile);
        for j=1:length(subfile)
            imgname=subfile(j).name;
            if length(imgname)>2 && subfile(j).isdir==0
                ImgStruct{end+1}=imgname;
                pathcell{end+1}=locfind(imgname);
            end
        end
    end
    ImgStructJson=jsonencode(ImgStruct);
end
function loc=locfind(str)
    ind=strfind(str,'(');
    loc=str(1:ind-2);
end
