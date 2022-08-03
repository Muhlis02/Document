#include <iostream>
#include <string>

using namespace std;

int main(){
	string nama;
	string ttl;
	string jeniskelamin;
	string alamat;
	string agama;
	string statusperkawinan;
	string pekerjaan;
	string kewarganegaraan;
	string jurusan;
	string npm;
	
	cout<<"Universitas Islam Madura Tekhnik Informatika A :"<<endl<<endl;
	cout<<"Nama :";
	getline (cin,nama);
	
	cout<<"Ttl :";
	getline (cin,ttl);
	
	cout<<"Jenis Kelamin :";
	getline (cin,jeniskelamin);
	
	cout<<"Alamat :";
	getline (cin,alamat);
	
	cout<<"Agama :";
	getline (cin,agama);
	
	cout<<"Status Perkawinan :";
	getline (cin,statusperkawinan);
	
	cout<<"Pekerjaan :";
	getline (cin,pekerjaan);
	
	cout<<"Kewarganegaraan :";
	getline (cin,kewarganegaraan);
	
	cout<<"Jurusan :";
	getline (cin,jurusan);
	
	cout<<"Npm :";;
	getline (cin,npm);
	
	cout<<endl;
	cout<<"Data Mahasiswa Universitas Islam Madura Tekhnik Informatika A"<<endl;
	cout<<"------------------------------"<<endl;
	
	cout<<"Nama :"<<nama<<endl;
	cout<<"Ttl :"<<ttl<<endl;
	cout<<"Jenis Kelamin :"<<jeniskelamin<<endl;
	cout<<"Alamat :"<<alamat<<endl;
	cout<<"Agama :"<<agama<<endl;
	cout<<"Status Perkawinan :"<<statusperkawinan<<endl;
	cout<<"Pekerjaan :"<<pekerjaan<<endl;
	cout<<"Kewarganegaraan :"<<kewarganegaraan<<endl;
	cout<<"Jurusan :"<<jurusan<<endl;
	cout<<"Npm :"<<npm<<endl;
	
}
