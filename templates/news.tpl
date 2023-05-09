<!DOCTYPE html>
<html>
<head>
    <title>Headlines</title>
</head>
<body>
    <h1>My Squad</h1>
    <ul>
        % for headline in headlines:
            <li>{{ headline }}</li>
        % end
    </ul>
</body>
</html>
