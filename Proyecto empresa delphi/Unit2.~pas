unit Unit2;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids, DBGrids, DB, PSQLDbTables, StdCtrls, Mask, DBCtrls,
  DBClient;

type
  TForm2 = class(TForm)
    PSQLDatabase1: TPSQLDatabase;
    DBGrid1: TDBGrid;
    Button1: TButton;
    Consulta2: TPSQLQuery;
    Button2: TButton;
    Button3: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form2: TForm2;

implementation

uses Unit1, Unit3;

{$R *.dfm}


{consigna 6}
procedure TForm2.Button1Click(Sender: TObject);
begin
   Consulta2.SQL.Clear;
   Consulta2.SQL.Text := 'SELECT COUNT(*) FROM usuarios';
   Consulta2.Open;
   ShowMessage('La cantidad de registros son: ' + IntToStr(Consulta2.Fields[0].AsInteger));
end;

{consigna 5}
procedure TForm2.Button2Click(Sender: TObject);
begin
    Consulta2.SQL.Clear;
    Consulta2.SQL.Add('SELECT MAX(codigousuario) FROM usuarios');
    Consulta2.Open;
    ShowMessage('El numero recomendado de id es: ' + (IntToStr(Consulta2.Fields[0].AsInteger + 1 )));
    {Form1.Edit1.Text := IntToStr(Consulta2.Fields[0].AsInteger + 1 );}
    Form3.Edit1.Text := IntToStr(Consulta2.Fields[0].AsInteger + 1 );
end;

{consigna 4}
procedure TForm2.Button3Click(Sender: TObject);
begin
    Consulta2.SQL.Clear;
    Consulta2.SQL.Add('SELECT codigousuario FROM usuarios WHERE codigousuario = ' + Form1.Edit1.Text);
    Consulta2.Open;
    if (Consulta2.Fields[0].AsInteger <> 0) then
        ShowMessage('El id ya esta en uso, ingresa otro.');
        //end if}
end;

end.
