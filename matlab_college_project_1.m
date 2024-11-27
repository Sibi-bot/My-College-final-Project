% Data
age_groups = {'21-25', '26-30', '31-35', '36-40', '41-45',
              '46-50', '51-55', '56-60', '61-65', '66-70'};
total_values = [0.77037, 0.81719, 0.71580, 0.73605, 0.72118, 
                0.79352, 0.70796, 0.73897, 0.74803, 0.77177];
rankings = [4, 1, 9, 7, 8, 2, 10, 6, 5, 3];
% Create the bar graph
figure;
bar(total_values, 'b');
% Set the x-tick labels
set(gca, 'XTickLabel', age_groups);
% Title and labels
title('Total Values by Age Group with Rankings');
xlabel('Age Group');
ylabel('Total');
% Display rankings on the bars
for i = 1:length(total_values)
    text(i, total_values(i) + 0.02, num2str(rankings(i)), 'HorizontalAlignment', 'center');
end
% Display grid
grid on;
% Show the figure
hold off;