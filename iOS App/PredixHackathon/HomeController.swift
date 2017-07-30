//
//  ViewController.swift
//  PredixHackathon
//
//  Created by Yazan Altwil on 7/29/17.
//  Copyright © 2017 Yazan Altwil. All rights reserved.
//

import UIKit

class HomeController: UICollectionViewController, UICollectionViewDelegateFlowLayout {
    
    let titles = ["Storage 1", "Storage 2"]
    let Storage1cellId = "Storage1cellId"
    let storage2CellId = "storage2CellId"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Storage 1"
        collectionView?.isPagingEnabled = true
        navigationItem.rightBarButtonItem = UIBarButtonItem(title: "Details", style: .plain, target: self, action: #selector(handleDetails))
        collectionView?.register(Storage1.self, forCellWithReuseIdentifier: Storage1cellId)
        collectionView?.register(Storage2.self, forCellWithReuseIdentifier: storage2CellId)
        
    }
    
    func handleDetails() {
        UIApplication.shared.openURL(NSURL(string: "https://app.powerbi.com/groups/me/dashboards/a8d9967d-f4cd-4c7e-9dd8-0a3d9d44f393")! as URL)
//        let dummySettingsViewController = DummyView()
//        dummySettingsViewController.navigationItem.title = title
//        
//        let navigationController = UIApplication.shared.keyWindow?.rootViewController as! UINavigationController
//        navigationController.navigationBar.tintColor = .black
//        navigationController.navigationBar.titleTextAttributes = [NSForegroundColorAttributeName: UIColor.black]
//        navigationController.pushViewController(dummySettingsViewController, animated: true)
    }

    
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    private func setTitleOfIndex(index: Int) {
        navigationItem.title = "  \(titles[index])"
    }
    
    override func scrollViewWillEndDragging(_ scrollView: UIScrollView, withVelocity velocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>) {
        collectionView?.reloadData()
        let index = targetContentOffset.pointee.x / view.frame.width
        setTitleOfIndex(index: Int(index))
    }

    
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 2
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        
        var identifier = ""
        if indexPath.item == 0 {
            identifier = Storage1cellId
        } else if indexPath.item == 1 {
            identifier = storage2CellId
        }
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: identifier, for: indexPath)
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: view.frame.width, height: view.frame.height - topLayoutGuide.length)
    }
    
    override func willTransition(to newCollection: UITraitCollection, with coordinator: UIViewControllerTransitionCoordinator) {
        collectionView?.collectionViewLayout.invalidateLayout()
        let indexPath = IndexPath(item: 0, section: 0)
        DispatchQueue.main.async {
            self.collectionView?.scrollToItem(at: indexPath, at: .centeredHorizontally, animated: true)
        }
    }
    
    
}
