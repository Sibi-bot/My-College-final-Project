% Data
ageGroups = {'21-25', '26-30', '31-35', '36-40', '41-45', '46-50', ...
'51-55', '56-60', '61-65', '66-70'};
totalValues = [48.13571781, 48.22750978, 50.07629593, 52.69502285, 57.0162524, ...
    62.55086449, 54.65985529, 64.30309906, 51.74719162, 53.89422953];
rankings = [10, 9, 8, 6, 3, 2, 4, 1, 7, 5];

% Create a bar graph
figure;
bar(totalValues, 'FaceColor', [0.2 0.6 0.8]); % Customize color if needed
set(gca, 'XTickLabel', ageGroups, 'XTick', 1:length(ageGroups)); % Set x-axis labels
xlabel('Age Groups');
ylabel('Total');
title('Total by Age Group');
grid on;

% Annotate with rankings
for i = 1:length(rankings)
    text(i, totalValues(i) + 0.5, num2str(rankings(i)), ...
        'HorizontalAlignment', 'center', 'Color', 'black');
end

% Adjust Y-axis limits for better visualization
ylim([0 max(totalValues) + 10]);

% Rotate X-axis labels for better readability
xtickangle(45);
