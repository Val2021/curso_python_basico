<!DOCTYPE html>
<html>
<head>
  <title>Tabela Verdade</title>
  <style>
    table {
      border-collapse: collapse;
    }
    
    th, td {
      border: 1px solid black;
      padding: 8px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h2>Tabela Verdade</h2>
  
  <table>
    <tr>
      <th>P</th>
      <th>Q</th>
      <th>P AND Q</th>
      <th>P OR Q</th>
      <th>NOT P</th>
    </tr>
    <tr>
      <td>true</td>
      <td>true</td>
      <td>true</td>
      <td>true</td>
      <td>false</td>
    </tr>
    <tr>
      <td>true</td>
      <td>false</td>
      <td>false</td>
      <td>true</td>
      <td>false</td>
    </tr>
    <tr>
      <td>false</td>
      <td>true</td>
      <td>false</td>
      <td>true</td>
      <td>true</td>
    </tr>
    <tr>
      <td>false</td>
      <td>false</td>
      <td>false</td>
      <td>false</td>
      <td>true</td>
    </tr>
  </table>
</body>
</html>

