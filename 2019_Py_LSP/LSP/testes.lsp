;; FeatureLine
(vlax-invoke-method (vlax-ename->vla-object(car(entsel))) 'GetPoints 0)
(vlax-variant-value (vlax-invoke-method (vlax-ename->vla-object(car(entsel))) 'GetPoints 0) )
(safearray-value (vlax-variant-value(vlax-invoke-method (vlax-ename->vla-object(car(entsel))) 'GetPoints 0)))

 
(vlax-invoke (vlax-ename->vla-object(car(entsel))) 'GetPoints)


;;; IntersectWith
(vlax-variant-value (vla-IntersectWith (vlax-ename->vla-object(car(entsel))) (vlax-ename->vla-object(car(entsel))) acExtendNone))

;;; Center
(safearray-value (vlax-variant-value(vla-get-center (vlax-ename->vla-object(car(entsel)))))
                 
;;; Get Handle
(vla-get-handle(vlax-ename->vla-object(car(entsel))))
