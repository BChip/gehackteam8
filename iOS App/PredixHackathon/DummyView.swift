//
//  DummyView.swift
//  PredixHackathon
//
//  Created by Yazan Altwil on 7/29/17.
//  Copyright © 2017 Yazan Altwil. All rights reserved.
//

import UIKit

class DummyView: UIViewController {
    let customCell = CustomCell()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = UIColor.rgb(red: 66, green: 66, blue: 66)
        view.addSubview(tempLabel)
        _ = tempLabel.anchor(topLayoutGuide.bottomAnchor, left: view.leftAnchor, bottom: nil, right: view.rightAnchor, topConstant: 20, leftConstant: 30, bottomConstant: 0, rightConstant: 30, widthConstant: 0, heightConstant: 45)
        view.addSubview(graphImage)
        _ = graphImage.anchor(tempLabel.bottomAnchor, left: view.leftAnchor, bottom: nil, right: view.rightAnchor, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 0, heightConstant: 270)
        
        view.addSubview(TemperatureTitle)
        _ = TemperatureTitle.anchor(graphImage.bottomAnchor, left: view.leftAnchor, bottom: nil, right: nil, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        
        view.addSubview(temp6hrs)
        _ = temp6hrs.anchor(TemperatureTitle.bottomAnchor, left: view.leftAnchor, bottom: nil, right: nil, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        view.addSubview(temp12hrs)
        _ = temp12hrs.anchor(temp6hrs.bottomAnchor, left: view.leftAnchor, bottom: nil, right: nil, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        
        view.addSubview(sensitivityLabel)
        _ = sensitivityLabel.anchor(temp12hrs.bottomAnchor, left: view.leftAnchor, bottom: view.bottomAnchor, right: view.rightAnchor, topConstant: 10, leftConstant: 10, bottomConstant: 0, rightConstant: 5, widthConstant: 0, heightConstant: 80)
        
        view.addSubview(HumidTitle)
        _ = HumidTitle.anchor(graphImage.bottomAnchor, left: nil, bottom: nil, right: view.rightAnchor, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        view.addSubview(humid6hrs)
        _ = humid6hrs.anchor(HumidTitle.bottomAnchor, left: nil, bottom: nil, right: view.rightAnchor, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        view.addSubview(humid12hrs)
        _ = humid12hrs.anchor(humid6hrs.bottomAnchor, left: nil, bottom: nil, right: view.rightAnchor, topConstant: 10, leftConstant: 10, bottomConstant: 10, rightConstant: 5, widthConstant: 175, heightConstant: 45)
        
        tempLabel.text = navigationItem.title
    }

    let tempLabel: UILabel = {
        let label = UILabel()
//        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.layer.borderWidth = 2;
        label.layer.borderColor = UIColor.white.cgColor
        label.textAlignment = .center
        label.textColor = .white
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 20)
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
        return label
    }()
    
    let sensitivityLabel: UILabel = {
        let label = UILabel()
        //        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.layer.borderWidth = 2;
        label.layer.borderColor = UIColor.white.cgColor
        label.textColor = .white
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 20)
        label.text = "  Sensitivity Level: "
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
        return label
    }()
    
    let TemperatureTitle: UILabel = {
        let label = UILabel()
        //        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.layer.borderWidth = 2
        label.layer.borderColor = UIColor.white.cgColor
        label.textAlignment = .center
        label.textColor = .white
        label.text = "Temperature"
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 20)
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
        return label
    }()
    
    let HumidTitle: UILabel = {
        let label = UILabel()
        //        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
        label.layer.borderWidth = 2
        label.layer.borderColor = UIColor.white.cgColor
        label.textAlignment = .center
        label.textColor = .white
        label.text = "Humidity"
        label.font = UIFont(name: "HelveticaNeue-Bold", size: 20)
        label.layer.cornerRadius = 5
        label.clipsToBounds = true
        return label
    }()

    
    let graphImage: UIImageView = {
        let iv = UIImageView()
        iv.layer.borderColor = UIColor.white.cgColor
        iv.layer.borderWidth = 2
        iv.layer.cornerRadius = 5
        iv.clipsToBounds = true
        return iv
    }()
    
//    let TempAvg6Hrs: UILabel = {
//        let label = UILabel()
//        //        label.backgroundColor = UIColor.rgb(red: 0, green: 191, blue: 255)
//        label.layer.borderWidth = 2;
//        label.layer.borderColor = UIColor.white.cgColor
//        label.textAlignment = .center
//        label.textColor = .white
//        label.text = "6 hrs"
//        label.font = UIFont(name: "HelveticaNeue-Bold", size: 20)
//        label.layer.cornerRadius = 5
//        label.clipsToBounds = true
//        return label
//    }()
//    
    let temp6hrs: UIButton = {
        let button = UIButton()
        button.layer.borderWidth = 2
        button.layer.borderColor = UIColor.white.cgColor
        button.contentHorizontalAlignment = UIControlContentHorizontalAlignment.center
        button.setTitleColor(.white, for: .normal)
        button.setTitle("6 Hrs", for: .normal)
        button.titleLabel?.font =  UIFont(name: "HelveticaNeue-Bold", size: 20)
        button.layer.cornerRadius = 5
        button.clipsToBounds = true
        return button
    }()
    
    let humid6hrs: UIButton = {
        let button = UIButton()
        button.layer.borderWidth = 2
        button.layer.borderColor = UIColor.white.cgColor
        button.contentHorizontalAlignment = UIControlContentHorizontalAlignment.center
        button.setTitleColor(.white, for: .normal)
        button.setTitle("6 Hrs", for: .normal)
        button.titleLabel?.font =  UIFont(name: "HelveticaNeue-Bold", size: 20)
        button.layer.cornerRadius = 5
        button.clipsToBounds = true
        return button
    }()
    
    
    let temp12hrs: UIButton = {
        let button = UIButton()
        button.layer.borderWidth = 2
        button.layer.borderColor = UIColor.white.cgColor
        button.contentHorizontalAlignment = UIControlContentHorizontalAlignment.center
        button.setTitleColor(.white, for: .normal)
        button.setTitle("12 Hrs", for: .normal)
        button.titleLabel?.font =  UIFont(name: "HelveticaNeue-Bold", size: 20)
        button.layer.cornerRadius = 5
        button.clipsToBounds = true
        return button
    }()
    
    let humid12hrs: UIButton = {
        let button = UIButton()
        button.layer.borderWidth = 2
        button.layer.borderColor = UIColor.white.cgColor
        button.contentHorizontalAlignment = UIControlContentHorizontalAlignment.center
        button.setTitleColor(.white, for: .normal)
        button.setTitle("12 Hrs", for: .normal)
        button.titleLabel?.font =  UIFont(name: "HelveticaNeue-Bold", size: 20)
        button.layer.cornerRadius = 5
        button.clipsToBounds = true
        return button
    }()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}
