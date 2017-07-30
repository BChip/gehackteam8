//
//  Temperature.swift
//  PredixHackathon
//
//  Created by Yazan Altwil on 7/29/17.
//  Copyright © 2017 Yazan Altwil. All rights reserved.
//

import UIKit

class Storage1: FeedCell {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
//    override func fillTemData() {
//        let storageDat: [StorageData] = {
//            let storage1 = StorageData()
//            storage1.StorageName = "Storage 1"
//            storage1.Temperature = 70
//            storage1.Humidity = 70
//            let storage2 = StorageData()
//            storage2.StorageName = "Storage 2"
//            storage2.Temperature = 65
//            storage2.Humidity = 63
//            return [storage1, storage2]
//        }()
//        self.storageData = storageDat
//    }
    
    var temperature: Int?
    let type = "Temperature"
//    let Frequency = "2h"
    var StorageName = "STORAGE1"
   
    let headers = [
        "authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1NmY4NGYwOWNjY2M0MzM3OTU4MzQ1M2U3N2NlOGEzNyIsInN1YiI6ImFwcF9jbGllbnRfaWQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5pbmdlc3QiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZjNlMWVmMjctOTU0My00YjVlLWExNWYtMTg2ZWVlZWEzNmQzLnVzZXIiLCJ1YWEucmVzb3VyY2UiLCJvcGVuaWQiLCJ1YWEubm9uZSIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgudXNlciJdLCJjbGllbnRfaWQiOiJhcHBfY2xpZW50X2lkIiwiY2lkIjoiYXBwX2NsaWVudF9pZCIsImF6cCI6ImFwcF9jbGllbnRfaWQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjEwZDg1NGQxIiwiaWF0IjoxNTAxNDE3Mzk3LCJleHAiOjE1MDE0NjA1OTcsImlzcyI6Imh0dHBzOi8vNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0IiwiYXVkIjpbInVhYSIsIm9wZW5pZCIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMyIsImFwcF9jbGllbnRfaWQiXX0.YaHHM_6PUVctrTT1d1iCb_y4ELTkAHUNAUtcKfXz71Ski9RX_s-hfWGd92qre8A05TLv5msrQ-HWa0KNj8UBskLjkTqtdKKYOQjw_S0mye_674r1DCq1y1oIyrir3v0eTmctsm4NWyEnUQRlZmDxGKKWo43aPD1eJylbl_sjCZ4uduuyLqadLLZr3FINOwXVDAJxz0Egsd017hNT8V6H7Va4NRts5qJTX6iF8RSjrY3HEgwCT6IsBtQAgqUj-nl6i3K-uwu5sBZAC-_hEdiHDDrspLOonFuV15fXC6O-wLQoB5-pEtDB42unhK-qGOysblOSKYg7vaKEob-haFSnOA",
        "predix-zone-id": "f3e1ef27-9543-4b5e-a15f-186eeeea36d3",
        "content-type": "application/json",
        "cache-control": "no-cache",
        "postman-token": "a9dc0bac-e80c-037d-cf5e-0c1009957135"
    ]

    
//    override func fillData() {
//        let storageDat: [StorageData] = {
//            let storage1 = StorageData()
//            storage1.StorageName = "test 1"
//            return [storage1]
//        }()
//        self.storageData = storageDat
//    }
    func fillTemperature(frequency: String) {
        
        let parameters: [String : Any] = [
            "tags": [
                [
                    "name": "\(type):\(StorageName)",
                    "aggregations": [
                        [
                            "type": "avg",
                            "interval": "\(frequency)"
                        ]
                    ],
                    "results": "values"
                ]
            ],
            "start": "\(frequency)-ago"
            ] as [String : Any]
        guard let url = URL(string: "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.allHTTPHeaderFields = headers

        guard let httpBody = try? JSONSerialization.data(withJSONObject: parameters, options: []) else { return }
        request.httpBody = httpBody
        
        
        let session = URLSession.shared
        session.dataTask(with: request) { (data, response, error) in
            if let response = response {
//                print(response)
            }
            if let data = data {
                do {
                    let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
                    let tags = json?["tags"] as! [Any]
                    let preResults = tags[0] as! [String: Any]
                    let results = preResults["results"] as! [Any]
                    let preValues = results[0] as! [String: Any]
                    let values = preValues["values"] as! [Any]
                    let finalValues = [values][0] as! [NSArray]
                    for val in finalValues {
                        self.temperature = val[1] as? Int
                    }
                    DispatchQueue.main.async {
                    }
                } catch {
                    print(error)
                }
            }
            }.resume()   
        
    }
    
    override func fillData(frequency: String) {
        fillTemperature(frequency: "\(frequency)")
        let parameters = [
            "tags": [
                [
                    "name": "\(type):\(StorageName)",
                    "aggregations": [
                        [
                            "type": "avg",
                            "interval": "\(frequency)"
                        ]
                    ],
                    "results": "values"
                ]
            ],
            "start": "\(frequency)-ago"
            ] as [String : Any]
        
        guard let url = URL(string: "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        //        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.allHTTPHeaderFields = headers
        
        guard let httpBody = try? JSONSerialization.data(withJSONObject: parameters, options: []) else { return }
        request.httpBody = httpBody
        
        
        let session = URLSession.shared
        session.dataTask(with: request) { (data, response, error) in
            if let response = response {
                print(response)
            }
            if let data = data {
                do {
                    let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
                    let tags = json?["tags"] as! [Any]
                    let preResults = tags[0] as! [String: Any]
                    let results = preResults["results"] as! [Any]
                    let preValues = results[0] as! [String: Any]
                    let values = preValues["values"] as! [Any]
                    let finalValues = [values][0] as! [NSArray]
                    var storageData = [StorageData]()
                    for val in finalValues {
                        let storage = StorageData()
                        storage.StorageName = self.StorageName
                        storage.Time = val[0] as? Int
                        storage.Humidity  = val[1] as? Int
                        storage.Temperature = self.temperature
                        storageData.append(storage)
                    }
                    DispatchQueue.main.async {
                        self.storageData = storageData
                        self.collectionView.reloadData()
                    }
                } catch {
                    print(error)
                }
            }
            }.resume()
    }
    
}
