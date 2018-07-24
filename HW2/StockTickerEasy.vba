Sub StockTickerEasy()
 ' LOOP THROUGH ALL SHEETS
 ' --------------------------------------------
Dim WS As Worksheet
    For Each WS In ActiveWorkbook.Worksheets
    WS.Activate
        ' Determine the Last Row <CNTL+SHIFT+END>
        LastRow = WS.Cells(Rows.Count, 1).End(xlUp).Row

        ' Add Heading for summary
        Cells(1, "I").Value = "Ticker"
        Cells(1, "J").Value = "Total Stock Volume"
        'Create Variable to hold Value
        Dim Ticker_Name As String
        Dim Volume As Double
        Volume = 0
        Dim Row As Double
        Row = 2
        Dim Column As Integer
        'Set to ticker column, note column 7 is volume and col 9 and 10 is where to put results
        Column = 1
        Dim i As Long
                
        For i = 2 To LastRow
         ' Validate that ticker is not the same, and if true start that ticker volume total
            If Cells(i + 1, Column).Value <> Cells(i, Column).Value Then
                ' Set Ticker name
                Ticker_Name = Cells(i, Column).Value
                Cells(Row, Column + 8).Value = Ticker_Name
                ' Add Total Volumn
                Volume = Volume + Cells(i, Column + 6).Value
                Cells(Row, Column + 9).Value = Volume
                ' Move to next row to list new ticker values
                Row = Row + 1
                ' reset the Volume Total
                Volume = 0
            'If same ticker than add to established total
            Else
                Volume = Volume + Cells(i, Column + 6).Value
            End If
        Next i
        
    Next WS
    
End Sub
