% BasicScienceVault – check the MATLAB setup (MAT01–MAT12)
% Run from the MATLAB command window:  run("setup/check_matlab_setup.m")
fprintf("MATLAB %s\n", version);
toolboxes = ["Signal_Toolbox", "Statistics_Toolbox", "Image_Toolbox", "Optimization_Toolbox"];
names     = ["Signal Processing", "Statistics and Machine Learning", "Image Processing", "Optimization"];
for k = 1:numel(toolboxes)
    fprintf("%-34s %s\n", names(k), string(license("test", toolboxes(k)) == 1));
end
third = ["eeglab", "ft_defaults", "spm", "PsychtoolboxVersion"];
for k = 1:numel(third)
    p = which(third(k));
    if isempty(p), p = "not on the path"; end
    fprintf("%-34s %s\n", third(k), p);
end
