//
//  CollectionViewCell.swift
//  PredixHackathon
//
//  Created by Yazan Altwil on 7/29/17.
//  Copyright © 2017 Yazan Altwil. All rights reserved.
//

import UIKit

class FeedCell: UICollectionViewCell, UICollectionViewDataSource, UICollectionViewDelegate, UICollectionViewDelegateFlowLayout {
    
    let cellId = "cellId"
    let Storage2Id = "Storage2Id"
    
    var storageData: [StorageData]?
    
    func fillData(frequency: String) {
        
    }
    func fillTemData() {
        
    }
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        fillData(frequency: "5h")
//        fillTemData()
        addSubview(collectionView)
        _ = collectionView.anchor(topAnchor, left: leftAnchor, bottom: bottomAnchor, right: rightAnchor, topConstant: 0, leftConstant: 0, bottomConstant: 0, rightConstant: 0, widthConstant: 0, heightConstant: 0)
        collectionView.register(CustomCell.self, forCellWithReuseIdentifier: cellId)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        layout.minimumLineSpacing = 0.5
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.translatesAutoresizingMaskIntoConstraints = false
        cv.backgroundColor = .white
        cv.contentInset = .zero
        cv.delegate = self
        cv.dataSource = self
        return cv
    }()
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return storageData?.count ?? 0
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! CustomCell
        cell.storageData = storageData?[indexPath.item]
//        cell.backgroundColor = UIColor.rgb(red: 66, green: 66, blue: 66)
        cell.backgroundColor = .white
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: frame.width, height: frame.height)
    }
    
    
    
}
