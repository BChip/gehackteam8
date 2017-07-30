//
//  CustomCell.swift
//  PredixHackathon
//
//  Created by Yazan Altwil on 7/29/17.
//  Copyright © 2017 Yazan Altwil. All rights reserved.
//

import UIKit

class CustomCell: UICollectionViewCell {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setUpViews()
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func fillTitle() -> String {
        var myTitle: String
        if let title = storageTitle.text {
            myTitle = title
        }
        myTitle = "failed"
        return myTitle
    }
    
    var storageData: StorageData? {
            didSet {
                self.storageTitle.text = storageData?.StorageName
                if let temperatureValue = storageData?.Temperature  {
                     self.tempLabel.text = "\(temperatureValue)°"
                }
                if let humidityVlaue = storageData?.Humidity     {
                    self.humidLabel.text = "\(humidityVlaue)%"
                }
            }
    }

    
    func setUpViews() {
        
//        addSubview(moreInfo)
//        _ = moreInfo.anchor(topAnchor, left: nil, bottom: nil, right: rightAnchor, topConstant: 10, leftConstant: 0, bottomConstant: 0, rightConstant: 10, widthConstant: 80, heightConstant: 40)
//        
//        addSubview(storageTitle)
//        _ = storageTitle.anchor(topAnchor, left: leftAnchor, bottom: nil, right: nil, topConstant: 10, leftConstant: 5, bottomConstant: 0, rightConstant: 30, widthConstant: 150, heightConstant: 45)
//        
        addSubview(tempLabel)
        _ = tempLabel.anchor(topAnchor, left: leftAnchor, bottom: nil, right: rightAnchor, topConstant: 10, leftConstant: 30, bottomConstant: 0, rightConstant: 30, widthConstant: 0, heightConstant: 280)
        
        addSubview(humidLabel)
        _ = humidLabel.anchor(tempLabel.bottomAnchor, left: leftAnchor, bottom: nil, right: rightAnchor, topConstant: 10, leftConstant: 30, bottomConstant: 0, rightConstant: 30, widthConstant: 0, heightConstant: 280)
    }
    
    let tempLabel: UILabel = {
        let label = UILabel()
//        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.textAlignment = .center
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 120)
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
//        label.textColor = UIColor.rgb(red: 255, green: 244, blue: 245)
        label.textColor = .red
        return label
    }()
    
    let humidLabel: UILabel = {
        let label = UILabel()
//        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 120)
        label.textAlignment = .center
        label.layer.cornerRadius = 5
//        label.textColor = UIColor.rgb(red: 244, green: 245, blue: 255)
        label.textColor = .blue
        label.clipsToBounds = true
        return label
    }()
    
    let storageTitle: UILabel = {
        let label = UILabel()
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
        label.font = UIFont(name:"HelveticaNeue-Bold", size: 16.0)
        return label
    }()
    
    
}
