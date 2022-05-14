unit Unit3;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, DateEdit, StdCtrls, DB, PSQLDbTables;

type
  TForm3 = class(TForm)
    PSQLDatabase1: TPSQLDatabase;
    PSQLQuery1: TPSQLQuery;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    DateEdit1: TDateEdit;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Edit1Change(Sender: TObject);
    procedure Edit2Change(Sender: TObject);
    procedure Edit3Change(Sender: TObject);
    procedure DateEdit1Change(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form3: TForm3;

implementation

uses Unit1;

{$R *.dfm}




procedure TForm3.Button1Click(Sender: TObject);
begin
   Form1.b_NuevoClick(Self);
end;

procedure TForm3.Button2Click(Sender: TObject);
begin
   Form1.b_ModificarClick(Self);
end;

procedure TForm3.Button3Click(Sender: TObject);
begin
   Form1.b_EliminarClick(Self);
end;

procedure TForm3.Edit1Change(Sender: TObject);
begin
    Form1.Edit1.Text:= Form3.Edit1.Text;
end;

procedure TForm3.Edit2Change(Sender: TObject);
begin
   Form1.Edit2.Text:= Form3.Edit2.Text;
end;

procedure TForm3.Edit3Change(Sender: TObject);
begin
   Form1.Edit3.Text:= Form3.Edit3.Text;
end;

procedure TForm3.DateEdit1Change(Sender: TObject);
begin
   Form1.DateEdit1.Date := Form3.DateEdit1.Date;
end;

end.
 