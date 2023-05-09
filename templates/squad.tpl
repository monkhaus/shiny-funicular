<!DOCTYPE html>
<html>
<head>
    <title>My Squad</title>
</head>
<body>
    <h1>My Squad</h1>
    <ul>
        % for player in players:
            <li>{{ player }}</li>
        % end
    </ul>
</body>
</html>
