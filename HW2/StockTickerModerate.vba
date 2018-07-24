Sub StockTicker()
    ' LOOP THROUGH ALL SHEETS
    ' --------------------------------------------
Dim WS As Worksheet
    For Each WS In ActiveWorkbook.Worksheets
    WS.Activate
        ' Determine the Last Row <CNTL+SHIFT+END>
        LastRow = WS.Cells(Rows.Count, 1).End(xlUp).Row

        'Add Heading for summary
        Cells(1, "I").Value = "Ticker"
        Cells(1, "J").Value = "Yearly Change"
        'New col value
        Cells(1, "K").Value = "Percent Change"
        Cells(1, "L").Value = "Total Stock Volume"
        'Create Variable to hold Value
        Dim OpenPrice As Double
        Dim ClosePrice As Double
        Dim YearlyChange As Double
        Dim TickerName As String
        Dim PercentChange As Double
        Dim Volume As Double
        Volume = 0
        Dim Row As Double
        Row = 2
        Dim Column As Integer
        'Set to ticker column, note column 7 is volume and col 9 and 10 is where to put results
        Column = 1
        Dim i As Long
        
        'Initialize Open Price
        OpenPrice = Cells(2, Column + 2).Value
        
        For i = 2 To LastRow
         'Validate that ticker is not the same, and if true start that ticker volume total
            If Cells(i + 1, Column).Value <> Cells(i, Column).Value Then
                'Set Ticker name
                TickerName = Cells(i, Column).Value
                Cells(Row, Column + 8).Value = TickerName
                'Set Close Price
                ClosePrice = Cells(i, Column + 5).Value
                'Add Yearly Change
                YearlyChange = ClosePrice - OpenPrice
                Cells(Row, Column + 9).Value = YearlyChange
                'Add Percent Change
                If (OpenPrice = 0 And ClosePrice = 0) Then
                    PercentChange = 0
                ElseIf (OpenPrice = 0 And ClosePrice <> 0) Then
                    PercentChange = 1
                Else
                    PercentChange = YearlyChange / OpenPrice
                    Cells(Row, Column + 10).Value = PercentChange
                    Cells(Row, Column + 10).NumberFormat = "0.00%"
                End If
                'Add Total Volume
                Volume = Volume + Cells(i, Column + 6).Value
                Cells(Row, Column + 11).Value = Volume
                'Move to next row to list new ticker values
                Row = Row + 1
                ' reset the Open Price
                OpenPrice = Cells(i + 1, Column + 2)
                ' reset the Volumn Total
                Volume = 0
            'If same ticker than add to established total
            Else
                Volume = Volume + Cells(i, Column + 6).Value
            End If
        Next i
        
        'Verify per WS the Last Row of Yearly Change
        YCLastRow = WS.Cells(Rows.Count, Column + 8).End(xlUp).Row
        'Set the Cell Colors
        For j = 2 To YCLastRow
            If (Cells(j, Column + 9).Value > 0 Or Cells(j, Column + 9).Value = 0) Then
                Cells(j, Column + 9).Interior.ColorIndex = 10
            ElseIf Cells(j, Column + 9).Value < 0 Then
                Cells(j, Column + 9).Interior.ColorIndex = 3
            End If
        Next j
               
    Next WS
        
End Sub
