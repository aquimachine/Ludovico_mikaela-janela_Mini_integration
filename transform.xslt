<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>Weather Data Integration Report</title>
            <style>
                body {
                    font-family: 'Brush Script MT', 'Georgia', 'Apple Chancery', cursive;
                    margin: 40px;
                    background-color: #f0cad5;
                    color: #333;

                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                }
                .container {
                    max-width: 800px;
                    background: #ffffff;
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                    margin: auto;
                }
                h1 {
                    color: #2c3e50; 
                    border-bottom: 2px solid #f56b94;
                    padding-bottom: 10px;
                    margin-top: 0;
                }
                table {
                    width: 100%;
                    border-collapse;
                    margin-top: 20px;
                }
                th, td {
                    padding: 12px 15px;
                    test-align: left;
                    border-bottom: 1px solid #e2e8f0; 
                }
                th {
                    background-color: #f56b94;
                    color: white;
                    text-transform: uppercase;
                    font-size: 15px;
                }
                tr:hover {
                    background-color: #f8fafc; 
                }
                .highlight {
                    font=weight: bold;
                    color: #569eda;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Weather Data Report for <xsl:value-of select="WeatherData/City"/>, <xsl:value-of select="WeatherData/Country"/></h1>
                <table>
                    <thead>
                        <tr>
                            <th>Weather Factor</th>
                            <th>Current Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Temperature</td>
                            <td class="highlight"><xsl:value-of select="WeatherData/Temperature"/> °C</td>
                        </tr>
                        <tr>
                            <td>Humidity</td>
                            <td><xsl:value-of select="WeatherData/Humidity"/>%</td>
                        </tr>
                        <tr>
                            <td>Current Condition</td>
                            <td><xsl:value-of select="WeatherData/Condition"/> (<xsl:value-of select="WeatherData/Description"/>)</td>
                        </tr>           
                        <tr>
                            <td>Wind Speed</td>
                            <td><xsl:value-of select="WeatherData/WindSpeed"/> m/s</td>
                        </tr>                                     
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

